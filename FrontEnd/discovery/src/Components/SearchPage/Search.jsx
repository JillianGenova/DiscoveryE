import React, { useState, useEffect } from 'react';
import GoogleMapReact from 'google-map-react';
import { useLocation, useHistory } from "react-router-dom";
import logo_orange from "../LandingPage/logo_orange.png"
import { TextField } from '@mui/material';
import "./Search.css"
import Marker from "../Map/Marker/Marker.jsx"
import BusinessButton from "./BusinessButton"
import getBusinesses from '../../api/getBusinesses';
import { Box } from '@mui/system';

const Search = () => {
    const location = useLocation(); // will need to get lat and long of user from this 
    const history = useHistory();

    useEffect(() => {
        console.log(getBusinesses(location, (b) => setBusinesses(b))); // hook
    }, []);

    const [businesses, setBusinesses] = useState([])

    return (
        <>
            <div class="topnav">
                <button className='addressBar'>
                    Showing results for: {location.state.params}
                </button>
                <button 
                    className='searchAgain'
                    onClick={() => history.push("/")}
                >
                    Change
                    <br/>
                    Address
                </button>
                <button 
                    className='homeButton'
                    onClick={() => history.push("/")}
                >
                    home
                </button>
                <img src={logo_orange} className="orangeImage"/>
            </div>
            <div class="sidebar">
                <div className="businessButtonContainer">
                    {
                        businesses.length > 0 && 
                        businesses.map((business) => (
                            <BusinessButton  
                                business={business}
                            />
                        ))
                    }
                </div>
            </div>
            <div style={{ height: '100vh', width: '100%'}}>
                <GoogleMapReact
                    bootstrapURLKeys={{ key: "AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0" }}
                    defaultCenter={{
                        // need to change to users location?
                        lat: 43.0731,
                        lng: -89.4012
                    }}
                    defaultZoom={15}
                >
                    {
                        businesses.length > 0 &&
                        businesses.map((business) => (
                            <Marker
                                text={business.name}
                                lat={business.location.lat}
                                lng={business.location.long}
                            />
                        ))
                    }
                </GoogleMapReact>
            </div>
        </>
        
    );
}

export default Search
