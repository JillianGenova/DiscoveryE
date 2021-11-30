import axios from "axios";
import Business from "../utils/Business"
import Location from "../utils/Location"

const getBusinesses = (location, setBusinessesCallback) => {

    axios.post('http://localhost:3000/search', {location})
            .then(function(response){
                const businesses = [];
                for (var i = 0; i < response.data.length; i++) {
                    const business = response.data[i];
                    businesses.push(
                        new Business(
                            business[0],
                            business[3],
                            new Location(
                                business[1], 
                                business[7], 
                                business[8]
                            )
                        )
                    );
                }
        
                setBusinessesCallback(businesses);
                
       //Perform action based on response
        })
        .catch(function(error){
            console.log(error);
       //Perform action based on error
        });
}

export default getBusinesses;