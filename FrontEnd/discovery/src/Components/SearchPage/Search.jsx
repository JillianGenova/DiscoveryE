import React, { useState, useEffect } from 'react';
import GoogleMapReact from 'google-map-react';
import { useLocation, useHistory } from "react-router-dom";
import "./Search.css"
import Marker from "../Map/Marker/Marker.jsx"
import BusinessButton from "./BusinessButton"
import getBusinesses from '../../api/getBusinesses';

const Search = () => {
    const location = useLocation(); // will need to get lat and long of user from this 

    // TODO
    const [search, setSearch] = useState(''); // users new location
    const history = useHistory();

    useEffect(() => {
        console.log(getBusinesses(location, (b) => setBusinesses(b))); // hook
    }, []);

    const [businesses, setBusinesses] = useState([])

    return (
        <>
            <div class="topnav">
                <a class="active" href="">hi</a>
            </div>
            <div class="sidebar">
                <div className="businessButtonContainer">
                    {
                        businesses.length > 0 && 
                        businesses.map((business) => (
                            <BusinessButton  
                                text={business.name}
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
