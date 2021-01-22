import React, { useState } from 'react';
import CreateIdeaForm from './CreateIdeaForm';
import "./Idea.css"


import { Dialog } from '@material-ui/core'
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

function IdeaFormModal({setIdeas}) {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }

  return (
    <>

        <div
          className="idea__form-btn"
          onClick={handleClickOpen}
        >Have an Idea?</div>

      <Dialog
        open={open}
        onClose={handleClose}
      >
        <DialogContent style={{width:"500px", height:"400px", display:"flex", justifyContent:"center"}}>
          <CreateIdeaForm setIdeas={setIdeas} onClose={handleClose} />
        </DialogContent>
      </Dialog>
    </>
  );
}

export default IdeaFormModal;
