import { Button, Box, TextField, Grid, Typography } from '@mui/material';
import SaveIcon from '@mui/icons-material/Save';
import DoDisturbIcon from '@mui/icons-material/DoDisturb';


export default function RecipeForm({ handleClose }) {

    const handleSubmit = async (event) => {
        event.preventDefault();
    }

    return (
        <Grid onSubmit={handleSubmit} autoComplete="off" component="form" sx={{
            '& > :not(style)': { m: 1 },
        }}>
            <Typography sx={{ textAlign: 'center' }} variant='h3'>Add a new recipe</Typography>
            <TextField label="Title" required name='title' fullWidth sx={{ mb: '.5rem' }} />
            <TextField label="Text" required name='text' fullWidth sx={{ mb: '.5rem' }} />
            <TextField label="Key" required name='key' fullWidth sx={{ mb: '.5rem' }} />

            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Button sx={{ mr: '.5rem', width: 'fit-content' }} type="submit" startIcon={<SaveIcon />} variant="contained">Save</Button>
                <Button sx={{ width: 'fit-content' }} onClick={handleClose} startIcon={<DoDisturbIcon />} variant="outlined">Cancel</Button>
            </div>

        </Grid>
    );
}
