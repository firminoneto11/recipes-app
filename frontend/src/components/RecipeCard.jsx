import {
    Button, Card, CardActions, CardContent, CardMedia, Grid, Typography
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

import Swal from 'sweetalert2';
import 'sweetalert2/dist/sweetalert2.css';


export default function RecipeCard({ recipe, axios, remove, idx }) {

    const deleteRecipe = async (id) => {
        try {
            var response = await axios.delete(`recipe/${id}/`);
        }
        catch (error) {
            console.log(error);
            return
        }
        if (response.status == 204) {
            remove(idx);
            Swal.fire(
                'Deleted!',
                `Recipe deleted!`,
                'success'
            );
        }
    }

    const deleteHandler = (id) => {
        Swal.fire({
            title: `Do you want to delete '${recipe.title}'?`,
            text: "If you delete it, you won't be able to see it again!",
            showDenyButton: true,
            confirmButtonText: 'Yes',
            denyButtonText: `No`,
        }).then(async ({ isConfirmed }) => {
            if (isConfirmed) {
                await deleteRecipe(id);
            }
        })
    }

    return (
        <Grid item xs={12} sm={6} md={4}>
            <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                <CardMedia component="img" image="https://source.unsplash.com/random/?food" alt="random" />
                <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                        {recipe.title}
                    </Typography>
                    <Typography>
                        {recipe.text}
                    </Typography>
                    <Typography>
                        {recipe.id}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" startIcon={<EditIcon />}>Edit</Button>
                    <Button onClick={() => deleteHandler(recipe.id)} size="small" startIcon={<DeleteIcon />}>Delete</Button>
                </CardActions>
            </Card>
        </Grid>
    );
}
