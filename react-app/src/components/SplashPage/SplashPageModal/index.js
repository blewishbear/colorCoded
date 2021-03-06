import React, { useState } from 'react';
import LoginForm from '../auth/LoginFormModal/LoginForm';

import { Dialog } from '@material-ui/core'
import DialogContent from '@material-ui/core/DialogContent';

function LoginFormDialog(props) {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }

  return (
    <>
      {!props.authenticated && (
        <button
          className="login-button"
          onClick={handleClickOpen}
        >Log In</button>
        )}
      
      <Dialog
        open={open}
        onClose={handleClose}
      >
        <DialogContent style={{width:"400px", height:"200px", display:"flex", justifyContent:"center", marginBottom: "30px"}}>
          <LoginForm {...props} onClose={handleClose} />
        </DialogContent>
      </Dialog>
    </>
  );
}

export default LoginFormDialog;
