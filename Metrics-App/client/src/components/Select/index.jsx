import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { CenteredContainer, SelectContainer, SpacingBetweenSelects, CenteredTable } from "./styles";
import BasicTable from "../Table";

const options = [
    { value: 'chocolate', label: 'Chocolate' },
    { value: 'strawberry', label: 'Strawberry' },
    { value: 'vanilla', label: 'Vanilla' }
]

const SelectComponent = () => {
    const [showTable1, setShowTable1] = useState(false);
    const [showTable2, setShowTable2] = useState(false);

    const handleClick1 = (e) => {
        if (e.target.value !== undefined) {
            setShowTable1(true);
        } else {
            setShowTable1(false);
        }
    }

    const handleClick2 = (e) => {
        if (e.target.value !== undefined) {
            setShowTable2(true);
        } else {
            setShowTable2(false);
        }
    }

    return (
        <div>
            <CenteredContainer>
                <SelectContainer>
                    <Autocomplete
                        disablePortal
                        style={{ backgroundColor: "white" }}
                        onChange={(e) => handleClick1(e)}
                        id="combo-box-demo"
                        options={options}
                        sx={{ width: 300 }}
                        renderInput={(params) => <TextField {...params} label="Biblioteca" />}
                    />
                </SelectContainer>
                <SpacingBetweenSelects />
                <SelectContainer>
                    <Autocomplete
                        disablePortal
                        style={{ backgroundColor: "white" }}
                        onChange={(e) => handleClick2(e)}
                        id="combo-box-demo"
                        options={options}
                        sx={{ width: 300 }}
                        renderInput={(params) => <TextField {...params} label="Biblioteca" />}
                    />
                </SelectContainer>
            </CenteredContainer>

            <CenteredTable>
                {showTable1 && <BasicTable />}
                {showTable2 && <BasicTable />}
            </CenteredTable>
        </div>
    )
}

export default SelectComponent;
