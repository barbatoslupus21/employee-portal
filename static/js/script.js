document.addEventListener('DOMContentLoaded', function() {
    const userInputs = document.querySelectorAll('.userInput');
    userInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            let value = this.value;

            this.value = value.split(' ').map(word => 
                word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
            ).join(' ');
        });
    });
});

function toggleArrow(button) {
    const arrow = button.querySelector('.arrow');
    arrow.classList.toggle('rotate');
}

document.getElementById('hamburger').addEventListener('click', function() {
    const main = document.querySelector('main');
    main.classList.toggle('sidebar-visible');
});

// calendar
document.addEventListener('DOMContentLoaded', function() {
    const monthYear = document.getElementById('monthYear');
    const calendarBody = document.getElementById('calendarBody');
    const prevMonth = document.getElementById('prevMonth');
    const nextMonth = document.getElementById('nextMonth');
    const todayButton = document.getElementById('today');
    const selectedDateElement = document.getElementById('selectedDate');
    const holidayList = document.getElementById('holidayList');

    let currentDate = new Date();
    let selectedDate = new Date();

    // Sample holidays (you can expand this)
    const holidays = {
        '2024-08-29': ['Satur-Day Off', 'Company Anniversary'],
        '2024-12-25': ['Christmas Day'],
        '2024-11-01': ['All Saints Day', 'Company Outing', 'Team Building'],
        // Add more holidays here
    };

    function generateCalendar(date) {
        const firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
        const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
       
        monthYear.textContent = `${date.toLocaleString('default', { month: 'long' })} ${date.getFullYear()}`;
       
        calendarBody.innerHTML = '';
       
        let dayCounter = 1;
        for (let i = 0; i < 6; i++) {
            const row = document.createElement('tr');
            for (let j = 0; j < 7; j++) {
                const cell = document.createElement('td');
                if (i === 0 && j < firstDay.getDay() - 1) {
                    // Empty cells before the first day
                    cell.textContent = '';
                } else if (dayCounter > lastDay.getDate()) {
                    // Empty cells after the last day
                    cell.textContent = '';
                } else {
                    const dateDiv = document.createElement('div');
                    dateDiv.classList.add('date');
                    dateDiv.textContent = dayCounter;
                    cell.appendChild(dateDiv);

                    const holidayKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(dayCounter).padStart(2, '0')}`;
                    if (holidays[holidayKey]) {
                        cell.style.backgroundColor = 'white';
                        cell.style.color = 'Red';
                        cell.style.fontWeight = 800;
                    }

                    if (date.getFullYear() === currentDate.getFullYear() &&
                        date.getMonth() === currentDate.getMonth() &&
                        dayCounter === currentDate.getDate()) {
                        cell.classList.add('today');
                    }

                    // Create a new date object for each cell
                    const cellDate = new Date(date.getFullYear(), date.getMonth(), dayCounter);
                    cell.addEventListener('click', () => {
                        selectedDate = cellDate;
                        updateHolidayCard();
                    });

                    dayCounter++;
                }
                row.appendChild(cell);
            }
            calendarBody.appendChild(row);
        }
    }

    function updateHolidayCard() {
        selectedDateElement.textContent = selectedDate.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        holidayList.innerHTML = '';

        const holidayKey = `${selectedDate.getFullYear()}-${String(selectedDate.getMonth() + 1).padStart(2, '0')}-${String(selectedDate.getDate()).padStart(2, '0')}`;
        if (holidays[holidayKey]) {
            holidays[holidayKey].forEach(holiday => {
                const li = document.createElement('li');
                li.classList.add('list-group-item');
                li.classList.add('py-2');
                li.classList.add('rounded');
                li.classList.add('border-0');
                li.textContent = holiday;
                holidayList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.classList.add('list-group-item');
            li.classList.add('py-2');
            li.classList.add('rounded');
            li.classList.add('border-0');
            li.textContent = 'No holidays on this date';
            holidayList.appendChild(li);
        }
    }

    generateCalendar(currentDate);
    updateHolidayCard();

    prevMonth.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        generateCalendar(currentDate);
    });

    nextMonth.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        generateCalendar(currentDate);
    });

    todayButton.addEventListener('click', () => {
        currentDate = new Date();
        selectedDate = new Date();
        generateCalendar(currentDate);
        updateHolidayCard();
    });
});


// time logs
document.addEventListener('DOMContentLoaded', function() {
    const monthYear = document.getElementById('monthYear');
    const timeBody = document.getElementById('timeBody');
    const prevMonth = document.getElementById('prevMonth');
    const nextMonth = document.getElementById('nextMonth');
    const todayButton = document.getElementById('today');
    const selectedDateElement = document.getElementById('selectedDate');
    const timelogsContainer = document.getElementById('timelogsContainer');

    let currentDate = new Date();
    let selectedDate = new Date();

    // Sample timelogs (with time in and time out)
    const timelogs = {
        '2024-08-23': { timeIn: '06:30 AM', timeOut: '04:30 PM', overtime: '1:00' },
        '2024-08-24': { timeIn: '06:45 AM', timeOut: '04:45 PM', overtime: '0:30' },
        '2024-08-25': { timeIn: '06:15 AM', timeOut: '04:15 PM', overtime: '0:00' },
        '2024-08-26': { timeIn: '06:30 AM',  overtime: '1:30' },
        // Add more timelogs here if needed
    };

    function generatetime(date) {
        const firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
        const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
       
        monthYear.textContent = `${date.toLocaleString('default', { month: 'long' })} ${date.getFullYear()}`;
       
        timeBody.innerHTML = '';
       
        let dayCounter = 1;
        for (let i = 0; i < 6; i++) {
            const row = document.createElement('tr');
            for (let j = 0; j < 7; j++) {
                const cell = document.createElement('td');
                if (i === 0 && j < firstDay.getDay() - 1) {
                    // Empty cells before the first day
                    cell.textContent = '';
                } else if (dayCounter > lastDay.getDate()) {
                    // Empty cells after the last day
                    cell.textContent = '';
                } else {
                    const dateDiv = document.createElement('div');
                    dateDiv.classList.add('date');
                    dateDiv.textContent = dayCounter;
                    cell.appendChild(dateDiv);

                    const timelogsKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(dayCounter).padStart(2, '0')}`;
                    if (timelogs[timelogsKey]) {
                        cell.style.color = 'royalblue';
                        cell.style.fontWeight = 800;
                    }

                    if (date.getFullYear() === currentDate.getFullYear() &&
                        date.getMonth() === currentDate.getMonth() &&
                        dayCounter === currentDate.getDate()) {
                        cell.classList.add('today');
                    }

                    // Create a new date object for each cell
                    const cellDate = new Date(date.getFullYear(), date.getMonth(), dayCounter);
                    cell.addEventListener('click', () => {
                        selectedDate = cellDate;
                        updateTimelogsCard();
                    });

                    dayCounter++;
                }
                row.appendChild(cell);
            }
            timeBody.appendChild(row);
        }
    }

    function updateTimelogsCard() {
        selectedDateElement.textContent = selectedDate.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        timelogsContainer.innerHTML = '';

        const timelogsKey = `${selectedDate.getFullYear()}-${String(selectedDate.getMonth() + 1).padStart(2, '0')}-${String(selectedDate.getDate()).padStart(2, '0')}`;
        if (timelogs[timelogsKey]) {
            const timelog = timelogs[timelogsKey];
            const cardHTML = `
            <div class="card border mb-3">
                <div class="card-body text-secondary">
                    <p class="card-text ${timelog.timeIn ? 'alert alert-primary' : 'alert alert-danger'} light-gray rounded-3">
                        ${timelog.timeIn ? `Time In: ${timelog.timeIn}` : 'You did not time in on this date'}
                    </p>
                    <p class="card-text ${timelog.timeOut ? 'alert alert-success' : 'alert alert-danger'} light-gray rounded-3">
                        ${timelog.timeOut ? `Time Out: ${timelog.timeOut}` : 'You did not time out on this date'}
                    </p>
                    <p class="card-text alert alert-warning light-gray rounded-3">
                        ${timelog.overtime ? `OverTime: ${timelog.overtime}` : 'No overtime recorded for this date'}
                    </p>
                </div>
            </div>
             `;
            timelogsContainer.innerHTML = cardHTML;
        } else {
            const notimeHTML = `
                    <div class="card-body text-secondary">
                        <p class="card-text alert alert-info light-gray rounded-3">There are no time logs available for this date.</p>
                    </div>
            `;
            timelogsContainer.innerHTML = notimeHTML;
        }
    }

    generatetime(currentDate);
    updateTimelogsCard();

    prevMonth.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        generatetime(currentDate);
    });

    nextMonth.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        generatetime(currentDate);
    });

    todayButton.addEventListener('click', () => {
        currentDate = new Date();
        selectedDate = new Date();
        generatetime(currentDate);
        updateTimelogsCard();
    });
});

// prf control number checking
document.addEventListener('DOMContentLoaded', function() {
    const ctrlNumberInput = document.getElementById('ctrl_no');
    if (ctrlNumberInput) {
        const radioButtons = document.querySelectorAll('input[name="prfform"]');
        const relevantRadioIds = ['pgibig_loan', 'sss_loan', 'e_loan', 'educ_loan', 'med_loan'];

        function toggleCtrlNumber() {
            const isRelevantChecked = relevantRadioIds.some(id => document.getElementById(id).checked);
           
            if (isRelevantChecked) {
                ctrlNumberInput.parentElement.classList.add('show');
                ctrlNumberInput.setAttribute('required', 'required');
                setTimeout(() => ctrlNumberInput.focus(), 300);
            } else {
                ctrlNumberInput.parentElement.classList.remove('show');
                ctrlNumberInput.removeAttribute('required');
            }
        }

        radioButtons.forEach(radio => {
            radio.addEventListener('change', toggleCtrlNumber);
        });

        toggleCtrlNumber();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const othersNumberInput = document.getElementById('prf_others');
    if (othersNumberInput) {
        const radioButtons2 = document.querySelectorAll('input[name="prfform"]');
        const othersRadio = ['others'];

        function toggleCtrlNumber() {
            const isRelevantChecked = othersRadio.some(id => document.getElementById(id).checked);
           
            if (isRelevantChecked) {
                othersNumberInput.parentElement.classList.add('show');
                othersNumberInput.setAttribute('required', 'required');
                setTimeout(() => othersNumberInput.focus(), 300);
            } else {
                othersNumberInput.parentElement.classList.remove('show');
                othersNumberInput.removeAttribute('required');
            }
        }

        radioButtons2.forEach(radio => {
            radio.addEventListener('change', toggleCtrlNumber);
        });

        toggleCtrlNumber();
    }
});


// prf
// Function to sort the table based on column index
function sortTable(columnIndex) {
    const table = document.getElementById("requestTable");
    const rows = Array.from(table.rows).slice(1);
    const sortedRows = rows.sort((a, b) => {
      const aText = a.cells[columnIndex].innerText.toLowerCase();
      const bText = b.cells[columnIndex].innerText.toLowerCase();
      return aText.localeCompare(bText);
    });
  
    sortedRows.forEach(row => table.tBodies[0].appendChild(row));
  }
  
// Function to search the table
function searchTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const table = document.getElementById("requestTable");
    const rows = table.getElementsByTagName("tr");
  
    for (let i = 1; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("td");
      let shouldDisplay = false;
      for (let j = 0; j < cells.length - 1; j++) {
        if (cells[j].innerText.toLowerCase().includes(filter)) {
          shouldDisplay = true;
          break;
        }
      }
      rows[i].style.display = shouldDisplay ? "" : "none";
    }
  }


// survey admin create
function updatePeriod() {
    // Get the selected quarter
    const quarterSelect = document.getElementById('quarterSelect').value;
    const periodSelect = document.getElementById('periodSelect');

    // Define quarter periods
    const periods = {
        'First Quarter': 'Apr-May-Jun',
        'Second Quarter': 'Jul-Aug-Sept',
        'Third Quarter': 'Oct-Nov-Dec',
        'Fourth Quarter': 'Jan-Feb-Mar'
    };

    // Update the period select box
    periodSelect.innerHTML = ''; // Clear existing options
    const newOption = document.createElement('option');
    newOption.value = periods[quarterSelect];
    newOption.text = periods[quarterSelect];
    periodSelect.appendChild(newOption);
}


// leave dates
document.addEventListener('DOMContentLoaded', function() {
    const durationSelect = document.getElementById('durationSelect');
    const underTimeInput = document.getElementById('underTimeInput');

    function toggleUnderTimeInput() {
        if (durationSelect.value === 'Under Time') {
            underTimeInput.classList.add('show');
            underTimeInput.focus();
        } else {
            underTimeInput.classList.remove('show');
            underTimeInput.value = '';
        }
    }

    durationSelect.addEventListener('change', toggleUnderTimeInput);

    // Initial check
    toggleUnderTimeInput();
});



// leave summary history
function sortType(columnIndex) {
    const table = document.getElementById("leaveHistoryTable");
    const rows = Array.from(table.rows).slice(1);
    const sortedRows = rows.sort((a, b) => {
      const aText = a.cells[columnIndex].innerText.toLowerCase();
      const bText = b.cells[columnIndex].innerText.toLowerCase();
      return aText.localeCompare(bText);
    });
  
    sortedRows.forEach(row => table.tBodies[0].appendChild(row));
  }
  
// Function to search the table
function searchTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const table = document.getElementById("leaveHistoryTable");
    const rows = table.getElementsByTagName("tr");
  
    for (let i = 1; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("td");
      let shouldDisplay = false;
      for (let j = 0; j < cells.length - 1; j++) {
        if (cells[j].innerText.toLowerCase().includes(filter)) {
          shouldDisplay = true;
          break;
        }
      }
      rows[i].style.display = shouldDisplay ? "" : "none";
    }
  }


  