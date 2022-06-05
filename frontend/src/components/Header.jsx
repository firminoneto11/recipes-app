import { Box, Container, Typography, Stack, Button } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import SearchField from './SearchField';


export default function Header({ openModal, setData, axios, getRecipes }) {

    return (
        <Box sx={{
            bgcolor: 'background.paper',
            pt: 8,
            pb: 6,
        }}>
            <Container maxWidth="sm">
                <Typography component="h1" variant="h2" align="center" color="text.primary" gutterBottom>
                    Recipes App
                </Typography>
                <Typography variant="h5" align="center" color="text.secondary" paragraph>
                    A website where you can store and search your recipes!
                </Typography>
                <Stack sx={{ pt: 4 }} direction="row" spacing={2} justifyContent="center">
                    <Button onClick={() => openModal()} variant="contained" startIcon={<AddIcon />}>Add new recipe</Button>
                </Stack>
                <Stack sx={{ pt: 4 }} direction="row" spacing={2} justifyContent="center">
                    <SearchField setData={setData} axios={axios} getRecipes={getRecipes} />
                </Stack>
            </Container>
        </Box>
    );
}
