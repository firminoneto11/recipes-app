import { Button, TextField, Grid, Typography } from '@mui/material';
import SaveIcon from '@mui/icons-material/Save';
import DoDisturbIcon from '@mui/icons-material/DoDisturb';

import Swal from 'sweetalert2';
import 'sweetalert2/dist/sweetalert2.css';


export default function RecipeForm({ handleClose, axios, setData, modalData }) {

    const initialData = {
        title: modalData?.title,
        text: modalData?.text,
        id: modalData?.id
    }

    const updateData = async (data) => {
        try {
            var response = await axios.put(`recipe/${initialData.id}/`, data);
        }
        catch (error) {
            console.log(error);
            const status = error.response.status;
            if (status === 400) {
                Swal.fire({
                    title: "Invalid key",
                    text: "In order to update the recipe, you must inform the correct recipe's key!",
                    icon: "error",
                })
            }
            return;
        }
        if (response.status === 200) {
            const returnedData = response.data;
            setData((prev) => {
                const updatedCard = {
                    id: returnedData.id,
                    title: returnedData.title,
                    text: returnedData.text
                }

                const otherCards = prev.filter(el => {
                    if (el.id === updatedCard.id) {
                        return false;
                    }
                    return true;
                });

                return [updatedCard, ...otherCards];

            });
            handleClose();
        }
    }

    const postData = async (data) => {
        try {
            var response = await axios.post('recipes/', data);
        }
        catch (error) {
            console.log(error);
            return;
        }
        if (response.status === 201) {
            const returnedData = response.data;
            setData((prev) => {
                const newCard = {
                    id: returnedData.id,
                    title: returnedData.title,
                    text: returnedData.text
                }
                return [newCard, ...prev];
            });
            handleClose();
        }
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        const form = event.target;
        const data = {
            title: form.title.value,
            text: form.text.value,
            key: form.key.value,
        }
        if (modalData) {
            await updateData(data);
        }
        else {
            await postData(data);
        }
    }

    return (
        <Grid onSubmit={handleSubmit} autoComplete="off" component="form" sx={{
            '& > :not(style)': { m: 1 },
        }}>
            <Typography sx={{ textAlign: 'center' }} variant='h4'>
                {modalData ? "Update recipe" : "Add a new recipe"}
            </Typography>
            <TextField label="Title" required name='title' fullWidth sx={{ mb: '.5rem' }} defaultValue={initialData.title} />
            <TextField label="Text" required name='text' fullWidth sx={{ mb: '.5rem' }} defaultValue={initialData.text} />
            <TextField label="Key" required name='key' fullWidth sx={{ mb: '.5rem' }} />

            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Button sx={{ mr: '.5rem', width: 'fit-content' }} type="submit" startIcon={<SaveIcon />} variant="contained">
                    Save
                </Button>
                <Button sx={{ width: 'fit-content' }} onClick={handleClose} startIcon={<DoDisturbIcon />} variant="outlined">
                    Cancel
                </Button>
            </div>

        </Grid>
    );
}
