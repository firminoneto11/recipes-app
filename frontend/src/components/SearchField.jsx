import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';


export default function SearchField({ setData, axios, getRecipes }) {

    const fetchRecipe = async (id) => {
        try {
            var response = await axios.get(`recipe/${id}/`);
        }
        catch (error) {
            console.log(error);
            const status = error.response.status;
            if (status === 404) {
                setData([]);
            }
            return;
        }
        if (response.status === 200) {
            setData([response.data]);
        }
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        const recipe = event.target.recipe.value;
        if (!recipe) {
            await getRecipes();
            return;
        }
        await fetchRecipe(recipe);
    }

    return (
        <Paper autoComplete='off' onSubmit={handleSubmit} component="form"
            sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 400 }}>
            <InputBase sx={{ ml: 1, flex: 1 }} placeholder="Search for a recipe by it's id" name='recipe' />
            <IconButton type="submit" sx={{ p: '10px' }}>
                <SearchIcon />
            </IconButton>
        </Paper>
    );
}
