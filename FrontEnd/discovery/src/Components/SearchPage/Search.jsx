import React, { useState, useEffect } from 'react';
import GoogleMapReact from 'google-map-react';
import { useLocation } from "react-router-dom";
import "./Search.css"
import Marker from "../Map/Marker/Marker.jsx"
import BusinessButton from "./BusinessButton"
import axios from "axios";

const Search = () => {
    const location = useLocation(); // will need to get lat and long of user from this 
    const [msg, setMsg] = useState('');
    const [businesses, setBusinesses] = useState(["Michael Angelo's Coffee House", "Ian's Pizza", "Fair Trade Coffee"])

    axios.post('http://localhost:3000/search', {location})
            .then(function(response){
                console.log(response);
                setMsg(response.data)
       //Perform action based on response
        })
        .catch(function(error){
            console.log(error);
       //Perform action based on error
        });

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
        <><h2>{msg}</h2></>
        /*
        <>
            <div class="topnav">
                <a class="active" href="#home">Home</a>
            </div>
            <div class="sidebar">
                <div className="buttonContainer">
                    {
                        businesses.map((business) => (
                            <BusinessButton
                                text={business}
                            />
                        ))
                    }
                </div>
            </div>
            <div style={{ height: '100vh', width: '100%'}}>
                <GoogleMapReact
                    bootstrapURLKeys={{ key: "TO ADD" }}
                    defaultCenter={{
                        lat: 43.0731,
                        lng: -89.4012
                    }}
                    defaultZoom={15}
                >
                    {
                        // update with business objects
                        // businesses.map((business) => (
                        //     <Marker
                        //         text={business.name}
                        //         lat={business.geometry.location.lat}
                        //         lng={business.geometry.location.lng}
                        //     />
                        // ))
                    }
                </GoogleMapReact>
            </div>
        </>
        */
    );
}

export default Search
