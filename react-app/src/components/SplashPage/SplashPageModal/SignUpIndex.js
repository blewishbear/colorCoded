import React, { useState } from "react";
import SignUpForm from "../auth/SignUpFormModal/SignUpForm";

import { Dialog } from "@material-ui/core";
import DialogContent from "@material-ui/core/DialogContent";


function SignUpFormDialog(props) {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <>
      {!props.authenticated && (
        <button className="sign__up-button" onClick={handleClickOpen}>
          Sign Up
        </button>
      )}
      <Dialog open={open} onClose={handleClose}>
        <DialogContent
          style={{
            width: "500px",
            height: "300px",
            display: "flex",
            justifyContent: "center",
            marginBottom: "30px",
          }}
        >
          <SignUpForm {...props} onClose={handleClose} />
        </DialogContent>
      </Dialog>
    </>
  );
}

export default SignUpFormDialog;
