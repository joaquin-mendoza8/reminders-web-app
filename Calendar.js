import React, { useEffect, useRef, useState } from 'react';
import 'fullcalendar'; // Import the FullCalendar library
import 'fullcalendar/dist/fullcalendar.css'; // Import the FullCalendar CSS

const Calendar = ({ onSelectDate }) => {
  const calendarRef = useRef(null);
  const [calendarVisible, setCalendarVisible] = useState(false);

  useEffect(() => {
    // Initialize the FullCalendar when the component mounts
    const calendarEl = calendarRef.current;

    const calendar = new window.FullCalendar.Calendar(calendarEl, {
      // Configure the FullCalendar options here
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      // Add other configuration options as needed
      selectable: true, // Allow date selection
      select: onSelectDate, // Callback function for date selection
    });

    calendar.render(); // Render the calendar

    return () => {
      // Clean up the FullCalendar instance when the component unmounts
      calendar.destroy();
    };
  }, [onSelectDate]);

  return (
    <div>
      <button id="calendar-button" onClick={() => setCalendarVisible(true)}>Select Date</button>
      <div id="calendar-container" className={calendarVisible ? 'visible' : ''}>
        <div ref={calendarRef}></div>
      </div>
    </div>
  );
};

export default Calendar;
