import { atom } from "recoil";



//atoms are like pieces of state like state and setState
export const cartState = atom({
  key: "cartState",
  //the state of the cart empty for now
  default: [],
});

export const productsState = atom({
  key: "productsState",

  default: [],
})
export const ideaState = atom({
  key: "ideaState",

  default: [],
})
