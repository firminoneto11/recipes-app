import { createContext } from "react";
import axios from "axios";


export const AxiosContext = createContext();


export const DataContextProvider = ({ children }) => {

    const API_HOST = import.meta.env.VITE_API_HOST;

    const axiosInstance = axios.create({
        baseURL: `${API_HOST}/api/`
    });

    const contextData = { axios: axiosInstance };

    return (
        <AxiosContext.Provider value={contextData}>
            {children}
        </AxiosContext.Provider>
    );

}
