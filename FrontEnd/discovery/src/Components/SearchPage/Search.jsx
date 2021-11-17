import React, { useState, useEffect } from 'react';
import GoogleMapReact from 'google-map-react';
import { useLocation } from "react-router-dom";
import "./Search.css"
import Marker from "../Map/Marker/Marker.jsx"

const Search = () => {
    // "AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0"
    const location = useLocation(); // will need to get lat and long of user from this 

    const [places, setPlaces] = useState([])

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
                <a class="active" href="#home">Home</a>
            </div>
            <div style={{ height: '90vh', width: '100%' }}>
                <GoogleMapReact
                    bootstrapURLKeys={{ key: "AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0" }}
                    defaultCenter={{
                        lat: 43.0731,
                        lng: -89.4012
                    }}
                    defaultZoom={15}
                >
                    {
                        // update with business objects
                        places.map((place) => (
                            <Marker
                                text={place.name}
                                lat={place.geometry.location.lat}
                                lng={place.geometry.location.lng}
                            />
                        ))
                    }
                </GoogleMapReact>
            </div>
        </>

    );
}

export default Search