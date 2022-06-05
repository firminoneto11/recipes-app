import { Fragment, useEffect, useContext, useState } from 'react';
import MenuBar from '../components/MenuBar';
import Footer from '../components/Footer';
import Header from '../components/Header';
import RecipeCard from '../components/RecipeCard';
import Spinner from '../components/Spinner';
import TransitionsModal from '../components/Modal';
import { Container, Grid, Typography } from '@mui/material';
import { AxiosContext } from '../context/DataContext';
import RecipeForm from '../components/RecipeForm';


export default function Index() {

    const { axios } = useContext(AxiosContext);
    const [isLoading, setIsLoading] = useState(true);
    const [data, setData] = useState([]);

    const [open, setOpen] = useState(false);

    const handleOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const getRecipes = async () => {
        try {
            var response = await axios.get('recipes/');
        }
        catch (error) {
            console.log(error);
            setIsLoading(false);
            return;
        }
        setIsLoading(false);
        if (response.data.length) {
            setData(response.data);
        }
        else {
            setData([]);
        }
    }

    const CenteredElements = ({ children }) => {
        return (
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                {children}
            </div>
        );
    }

    const removeRecipeFromDom = (idx) => {
        setData((prev) => {
            prev.splice(idx, 1);
            return [...prev];
        });
    }

    const noData = !isLoading && !data.length ? true : false;
    const hasData = !isLoading && data.length ? true : false;

    useEffect(() => {
        getRecipes();
    }, []);

    return (
        <Fragment>
            <TransitionsModal open={open} handleOpen={handleOpen} handleClose={handleClose}>
                <RecipeForm handleClose={handleClose} />
            </TransitionsModal>
            <MenuBar />
            <Header openModal={handleOpen} />
            <main>
                <Container sx={{ py: 8 }} maxWidth="md">

                    {/* Component is fetching */}
                    {isLoading && (
                        <CenteredElements>
                            <Spinner />
                        </CenteredElements>
                    )}

                    {/* Component fecthed the data, but got nothing */}
                    {noData && (
                        <CenteredElements>
                            <Typography variant='h6'>
                                No recipes found, but feel free to create some!
                            </Typography>
                        </CenteredElements>
                    )}

                    {/* Component got data */}
                    {hasData && (
                        <Grid container spacing={4}>
                            {data.map((el, idx) => (
                                <RecipeCard key={idx} idx={idx} recipe={el} axios={axios} remove={removeRecipeFromDom} />
                            ))}
                        </Grid>
                    )}

                </Container>
            </main>
            <Footer />
        </Fragment>
    );
}
