import React, { useState } from 'react';
import { TextField } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';

const SearchBar = ({search, setSearch, history}) => {

    return (
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
                    history.push("/results", { params: search });
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
    )
}

export default SearchBar;