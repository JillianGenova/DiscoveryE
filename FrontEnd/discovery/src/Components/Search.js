import React, { useState, useEffect } from "react";
import GoogleMapReact from "google-map-react";
import { useLocation } from "react-router-dom";
import "./Search.css";
import Marker from "../Map/Marker/Marker.jsx";
import BusinessButton from "./BusinessButton";
import axios from "axios";

function Search() {
    const location = useLocation(); // will need to get lat and long of user from this 

    const [businesses, setBusinesses] = useState(["Michael Angelo's Coffee House", "Ian's Pizza", "Fair Trade Coffee"])
    const [currentTime, setCurrentTime] = useState(0);
    const [msg, setMsg] = useState('');

    var myParams = {
        data: location.state.params
    }

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

    //fetch('/time').then(res => res.json()).then(data => {
    //  setMsg(data.time);
    //});

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
        //<h2>The current time is {msg}.</h2>
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

    );
}

// exporting home component for other files to use
export default Search
