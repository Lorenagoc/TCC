import React from 'react'
import { Container, Content } from './styles'
import {
    FaTimes,
    FaMapMarked,
    FaDatabase,
    FaSuitcase,
    FaRegFileCode,
    FaPuzzlePiece,
    FaUnlockAlt,
    FaChartBar,
    FaLock,
    FaCode,
    FaFile,
    FaMailBulk,
    FaBoxes,
    FaRobot
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
                <SidebarItem Icon={FaCode} Text={`${domains[0]}`} />
                <SidebarItem Icon={FaChartBar} Text={`${domains[1]}`}/>
                <SidebarItem Icon={FaSuitcase} Text={`${domains[2]}`}/>
                <SidebarItem Icon={FaPuzzlePiece} Text={`${domains[3]}`}/>
                <SidebarItem Icon={FaUnlockAlt} Text={`${domains[4]}`}/>
                <SidebarItem Icon={FaRegFileCode} Text={`${domains[5]}`}/>
                <SidebarItem Icon={FaDatabase} Text={`${domains[6]}`}/>
                <SidebarItem Icon={FaLock} Text={`${domains[7]}`}/>
                <SidebarItem Icon={FaMapMarked} Text={`${domains[8]}`}/>
                <SidebarItem Icon={FaFile} Text={`${domains[9]}`}/>
                <SidebarItem Icon={FaMailBulk} Text={`${domains[10]}`}/>
                <SidebarItem Icon={FaBoxes} Text={`${domains[11]}`}/>
                <SidebarItem Icon={FaRobot} Text={`${domains[12]}`}/>
            </Content>
        </Container>
    )
}

export default Sidebar