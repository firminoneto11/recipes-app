import Index from "./pages/Index";
import { DataContextProvider } from "./context/DataContext";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';


export default function App() {

    const theme = createTheme();

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <DataContextProvider>
                <Index />
            </DataContextProvider>
        </ThemeProvider>
    );
}
