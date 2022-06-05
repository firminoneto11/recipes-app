import MenuBookIcon from '@mui/icons-material/MenuBook';
import { AppBar, Toolbar, Typography } from '@mui/material';


export default function MenuBar() {

    return (
        <AppBar position="relative">
            <Toolbar>
                <MenuBookIcon sx={{ mr: 2 }} />
                <Typography variant="h6" color="inherit" noWrap>
                    Recipes App
                </Typography>
            </Toolbar>
        </AppBar>
    );
}