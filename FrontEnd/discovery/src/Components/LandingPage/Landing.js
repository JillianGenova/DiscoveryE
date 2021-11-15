import React, { useState, useEffect } from 'react';
import { TextField, Button } from '@mui/material';
import "./Landing.css";
import logo from "./Logo.png";
import { useHistory } from "react-router-dom";

const buttonStyle = {
    unclicked: {
        background: 'white',
        color: 'orange'
    },
    clicked: {
        background: 'orange',
        color: 'white'
    },
}
const Landing = () => {
    const filters = ["Food", "Clothing", "Gift", "Services", "Other"]
    const [pressed, setPressed] = useState(false);
    const [search, setSearch] = useState('');
    const history = useHistory();


    return (
        <div className="homePage">
            <img src={logo} />
            <div>
                <TextField
                    className="searchBox"
                    id="outlined-search"
                    label="Search field"
                    type="search"
                    size="small"
                    style={{ marginTop: '20px' }}
                    value={search}
                    onChange={(e) => {
                        setSearch(e.target.value);
                    }}
                    onKeyDown={(e) => {
                        //13 for enter
                        if (e.keyCode == 13) {
                            history.push("/results", { search });
                        }
                    }
                }
                />
            </div>
            <div className="buttonContainer">
                {
                    filters.map((filter) => {
                        return (
                            <Button className="button" variant="contained"
                                onClick={() => {
                                    setPressed(!pressed);
                                }}
                                style={pressed ? buttonStyle.clicked : buttonStyle.unclicked}>
                                {filter}
                            </Button>
                        )
                    })
                }
            </div>
        </div>
    );
}

export default Landing;