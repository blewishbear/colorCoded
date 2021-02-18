import React, { useState } from 'react';
import HomePage from './HomePage';

import { Dialog } from '@material-ui/core'
import DialogContent from '@material-ui/core/DialogContent';

function HomePageDialog(props) {
  const [open, setOpen] = useState(true);


  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }

  return (
    <>
      {/* {!props.authenticated && (
        <div
          className="usermenu__option"
          onClick={handleClickOpen}
        >Log In</div>
      )} */}
      <Dialog
        open={open}
        onClose={handleClose}
      >
        <DialogContent style={{backgroundColor: "beige", width:"600px", height:"1000px", display:"flex", justifyContent:"center", marginBottom: "30px"}}>
          <HomePage {...props} onClose={handleClose} />
        </DialogContent>
      </Dialog>
    </>
  );
}

export default HomePageDialog;
