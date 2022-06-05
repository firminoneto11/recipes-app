import { Backdrop, Box, Modal, Fade } from '@mui/material';


export default function TransitionsModal({ open, handleClose, children }) {

    const modalStyle = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 'fit-content',
        bgcolor: 'background.paper',
        borderRadius: '3px',
        boxShadow: 24,
        p: 4,
    };

    return (
        <div>
            <Modal open={open} onClose={handleClose} closeAfterTransition BackdropComponent={Backdrop}
                BackdropProps={{
                    timeout: 500,
                }}>
                <Fade in={open}>
                    <Box sx={modalStyle}>
                        {children}
                    </Box>
                </Fade>
            </Modal>
        </div>
    );

}
