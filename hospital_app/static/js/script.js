// Run after page loads
document.addEventListener("DOMContentLoaded", function () {

    // Select Bed
    const bedButtons = document.querySelectorAll(".bed-btn");

    bedButtons.forEach(btn => {
        btn.addEventListener("click", function () {
            bedButtons.forEach(b => b.classList.remove("active"));
            this.classList.add("active");
        });
    });

    // Confirm Booking
    const confirmBtn = document.querySelector(".confirm-btn");

    if (confirmBtn) {
        confirmBtn.addEventListener("click", function () {

            const selectedBed = document.querySelector(".bed-btn.active");
            const bed = selectedBed ? selectedBed.innerText : "";

            const date = document.getElementById("appointmentDate").value;
            const time = document.getElementById("appointmentTime").value;

            const modal = document.getElementById("confirmationModal");
            const details = document.getElementById("bookingDetails");

            if (bed && date && time) {

                details.innerHTML =
                    "Bed: " + bed + "<br>" +
                    "Date: " + date + "<br>" +
                    "Time: " + time;

                modal.style.display = "block";

            }
        });
    }

    // Close Modal
    const closeBtn = document.querySelector(".close");
    const modal = document.getElementById("confirmationModal");

    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

});
document.addEventListener("DOMContentLoaded", function () {
    // Select Bed
    const bedButtons = document.querySelectorAll(".bed-btn");
    bedButtons.forEach(btn => {
        btn.addEventListener("click", function () {
            bedButtons.forEach(b => b.classList.remove("active"));
            this.classList.add("active");
        });
    });

    // Select Time Slot
    const slotButtons = document.querySelectorAll(".slot-btn");
    slotButtons.forEach(btn => {
        btn.addEventListener("click", function () {
            slotButtons.forEach(s => s.classList.remove("active"));
            this.classList.add("active");
        });
    });

    // Confirm Booking
    const confirmBtn = document.querySelector(".confirm-btn");
    if (confirmBtn) {
        confirmBtn.addEventListener("click", function (event) {
            event.preventDefault();

            const doctor = document.getElementById("doctor").value;
            const department = document.getElementById("department").value;
            const problem = document.getElementById("problem").value;
            const selectedBed = document.querySelector(".bed-btn.active");
            const bed = selectedBed ? selectedBed.innerText : "";
            const date = document.getElementById("appointmentDate").value;
            const selectedSlot = document.querySelector(".slot-btn.active");
            const time = selectedSlot ? selectedSlot.innerText : "";

            const modal = document.getElementById("confirmationModal");
            const details = document.getElementById("bookingDetails");

            if (!doctor) {
                alert("Please select a doctor before confirming.");
                return;
            }
            if (!department) {
                alert("Please select a department before confirming.");
                return;
            }
            if (!bed || !date || !time) {
                alert("Please select bed, date, and time slot before confirming.");
                return;
            }

            // Show full booking details in modal
            details.innerHTML =
                "Doctor: " + doctor + "<br>" +
                "Department: " + department + "<br>" +
                "Problem: " + problem + "<br>" +
                "Bed: " + bed + "<br>" +
                "Date: " + date + "<br>" +
                "Time: " + time;

            modal.style.display = "block";
        });
    }

    // Close Modal
    const closeBtn = document.querySelector(".close");
    const modal = document.getElementById("confirmationModal");
    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
