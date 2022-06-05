import { Typography, Link } from '@mui/material';


export default function Copyright() {
    return (
        <Typography variant="body2" color="text.secondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://github.com/firminoneto11" target="_blank">
                Firmino Neto
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}
