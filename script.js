/*
    script.js - Defines the client-side functionality of the reminders page.
    Handles the creation of new reminders, and the deletion of existing ones.
*/

// Establish a connection to the server.
var socket = io.connect("http://localhost:8080/api/reminders");

function getReminders() {
    fetch("http://localhost:8080/api/reminders")
        .then(function(response) {
            if(response.ok) {
                return response.json();
            }
            throw new Error("Failed to retrieve reminders.");
        })
        .then(function(data) {
            console.log(data); // display data in console
        })
        .catch(function(error) {
            console.error(error);
        });
}

// TODO: use React to implement 'add' button

getReminders();

// handle unload event to close socket connection
window.addEventListener("unload", function() {
    socket.disconnect();
});