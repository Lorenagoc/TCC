import React, { useContext, useEffect, useState } from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { CenteredContainer, SelectContainer, SpacingBetweenSelects, CenteredTable } from "./styles";
import BasicTable from "../Table";
import { MetricsContext } from '../MetricsContext';


const SelectComponent = () => {
    const [showTable1, setShowTable1] = useState(false);
    const [showTable2, setShowTable2] = useState(false);
    const [values1, setValues1] = useState([]);
    const [values2, setValues2] = useState([]);
    const { selectedLibrary1, setSelectedLibrary1 } = useContext(MetricsContext);
    const { selectedLibrary2, setSelectedLibrary2 } = useContext(MetricsContext);
    const { data } = useContext(MetricsContext);
    const { domain } = useContext(MetricsContext);

    useEffect(() => {
        setValues1([]);
        setValues2([]);
        setShowTable1(false);
        setShowTable2(false);
    }, [domain]);

    const getNomes = () => {
        const nomes = [];
        data?.forEach((element) => {
            nomes.push({ value: element?.nomes, label: element?.nomes });
        });
        return nomes;
    }

    const handleChange1 = (e, value) => {
        setValues1(value);
        if (e.target.value !== undefined) {
            setShowTable1(true);
        } else {
            setShowTable1(false);
        }
    }

    const handleChange2 = (e, value) => {
        setValues2(value);
        if (e.target.value !== undefined) {
            setShowTable2(true);
        } else {
            setShowTable2(false);
        }
    }

    const handleInputChange1 = (libraryName) => {
        setSelectedLibrary1(data.find(library => library.nomes === libraryName));
    }

    const handleInputChange2 = (libraryName) => {
        setSelectedLibrary2(data.find(library => library.nomes === libraryName));
    }

    return (
        <div>
            <CenteredContainer>
                <SelectContainer>
                    <Autocomplete
                        disablePortal
                        style={{ backgroundColor: "white", borderRadius: "10px" }}
                        onChange={(event, newValue) => handleChange1(event, newValue)}
                        onInputChange={(event, newValue) => {
                            handleInputChange1(newValue);
                        }}
                        id="combo-box-demo"
                        options={getNomes()}
                        sx={{ width: 300 }}
                        renderInput={(params) => <TextField id="standard-search" {...params} label="Biblioteca" />}
                        value={values1}
                    />
                </SelectContainer>
                <SpacingBetweenSelects />
                <SelectContainer>
                    <Autocomplete
                        disablePortal
                        style={{ backgroundColor: "white", borderRadius: "10px" }}
                        onChange={(event, newValue) => handleChange2(event, newValue)}
                        onInputChange={(event, newValue) => {
                            handleInputChange2(newValue);
                        }}
                        id="combo-box-demo"
                        options={getNomes()}
                        sx={{ width: 300 }}
                        renderInput={(params) => <TextField id="standard-search" {...params} label="Biblioteca" />}
                        value={values2}
                    />
                </SelectContainer>
            </CenteredContainer>

            <CenteredTable>
                {showTable1 && <BasicTable selectedLibrary={selectedLibrary1} />}
                {showTable2 && <BasicTable selectedLibrary={selectedLibrary2} />}
            </CenteredTable>
        </div>
    )
}

export default SelectComponent;
