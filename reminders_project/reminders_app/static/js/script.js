/*
    script.js - Defines the client-side functionality of the reminders page.
    Handles the creation of new reminders, and the deletion of existing ones.
*/

import React from "react";
import ReactDOM from "react-dom";
import Add from "./Add.js";

// Render the 'add' button
ReactDOM.render(<Add />, document.getElementById("add"));

// Establish a connection to the server using Socket.io
var socket = io("http://localhost:8080");

function getReminders() {
  fetch("http://localhost:8080/api/reminders")
    .then(function (response) {
      if (response.ok) {
        return response.json();
      }
      throw new Error("Failed to retrieve reminders.");
    })
    .then(function (data) {
      console.log(data); // Display data in the console
    })
    .catch(function (error) {
      console.error(error);
    });
}

getReminders();

// Handle unload event to close socket connection
window.addEventListener("unload", function () {
  socket.disconnect();
});