import React, { useState, useEffect } from 'react';
import GoogleMapReact from 'google-map-react';
import { useLocation } from "react-router-dom";
import "./Search.css"
import Marker from "../Map/Marker/Marker.jsx"
import BusinessButton from "./BusinessButton"
import Business from '../../utils/Business';
import Location from '../../utils/Location';

const Search = () => {
    const location = useLocation(); // will need to get lat and long of user from this 

    let temp = new Business("Alumni Boardshop", "https://maps.google.com/?cid=2690018593773068425",
        new Location("1150 Williamson St, Madison, WI 53703, USA", 43.0797895, -89.3764259));

    const [businesses, setBusinesses] = useState([temp])

    // to get data:
    // const fetchPlaces = async () => {
    //     fetch('places.json')
    //         .then((response) => response.json())
    //         .then((data) => setPlaces(data.results))
    // }

    // when data is updated:
    // useEffect(() => {
    //     fetchPlaces();
    // }, [])

    return (
        //<h2>{location.state.params}</h2>
        <>
            <div class="topnav">
                <a class="active" href="#home">Home</a>
            </div>
            <div class="sidebar">
                <div className="businessButtonContainer">
                    {
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
                        lat: 43.0731,
                        lng: -89.4012
                    }}
                    defaultZoom={15}
                >
                    {
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
