import React from 'react'
import { Container, Content } from './styles'
import {
    FaTimes,
    FaHome,
    FaEnvelope,
    FaRegSun,
    FaUserAlt,
    FaIdCardAlt,
    FaRegFileAlt,
    FaRegCalendarAlt,
    FaChartBar
} from 'react-icons/fa'

import SidebarItem from '../SidebarItem';

const Sidebar = ({ active }) => {

    const domains = ['Testing', 'Logging', 'Utilities', 'Mocking', 'Cryptography', 'JSON', 'Databases', 'Security', 'Object-relational Mapping', 'XML Processing', 'Mail Client', 'Collections', 'Machine Learning'];

    const closeSidebar = () => {
        active(false)
    }

    return (
        <Container sidebar={active}>
            <FaTimes onClick={closeSidebar} />
            <Content>
                <SidebarItem Icon={FaHome} Text={`${domains[0]}`} />
                <SidebarItem Icon={FaChartBar} Text={`${domains[1]}`}/>
                <SidebarItem Icon={FaUserAlt} Text={`${domains[2]}`}/>
                <SidebarItem Icon={FaEnvelope} Text={`${domains[3]}`}/>
                <SidebarItem Icon={FaRegCalendarAlt} Text={`${domains[4]}`}/>
                <SidebarItem Icon={FaIdCardAlt} Text={`${domains[5]}`}/>
                <SidebarItem Icon={FaRegFileAlt} Text={`${domains[6]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[7]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[8]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[9]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[10]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[11]}`}/>
                <SidebarItem Icon={FaRegSun} Text={`${domains[12]}`}/>
            </Content>
        </Container>
    )
}

export default Sidebar