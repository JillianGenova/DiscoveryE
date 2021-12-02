import React, { useState } from 'react';
import "./Landing.css";
import logo from "./Logo.png";
import { useHistory } from "react-router-dom";
import StyledButton from '../Button/StyledButton';
import { TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';

const filters = ["food", "clothes", "gift", "services", "other"];

const Landing = () => {
    const [search, setSearch] = useState(''); // users location
    const [selectedFilters, setSelectedFilters] = useState([]); // THIS IS WHERE FILTERS ARE LOCATED

    const history = useHistory();

    const toggleFilter = (filter) => {
        if (selectedFilters.includes(filter)) {
            // deselect
            setSelectedFilters(selectedFilters.filter((filterLabel) => filterLabel !== filter));
        } else {
            // select
            setSelectedFilters([...selectedFilters, filter]);
        }
    };

    // useEffect(() => console.log(selectedFilters), [selectedFilters]);
    // use effect is checking when the state of the array (second param) is changed (run A if B changes)

    return (
        <div className="homePage">
            <img src={logo} />
            <div>
                <TextField
                    id="outlined-search"
                    label="Search field"
                    type="search"
                    size="small"
                    style={{ marginTop: '20px' }}
                    value={search}
                    onChange={(keyEvent) => {
                        setSearch(keyEvent.target.value);
                    }}
                    onKeyDown={(keyEvent) => {
                        // add key in addition to enter
                        if (keyEvent.key === 'Enter') {
                            history.push("/results", { params: search, selectedFilters });
                        }
                    }}
                    InputProps={{
                        endAdornment: <InputAdornment position="end">
                            <IconButton
                                onClick={() => history.push("/results", { params: search })}
                                edge="end"
                            >
                                <SearchIcon onClick={() => history.push("/results", { params: search })} />
                            </IconButton>
                        </InputAdornment>,
                    }}

                />
            </div>
            <div className="buttonContainer">
                {
                    filters.map((filter) => (
                        <StyledButton
                            text={filter}
                            onClick={() => toggleFilter(filter)}
                            checked={selectedFilters.includes(filter)}
                        />
                    ))
                }
            </div>
        </div>
    );
}

export default Landing;