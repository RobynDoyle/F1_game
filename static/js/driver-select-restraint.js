
    document.addEventListener('DOMContentLoaded', function () {
        const driverSelect = document.getElementById('driver');
        const driverTwoSelect = document.getElementById('driver_two');
        const driverThreeSelect = document.getElementById('driver_three');
        
        const allSelects = [driverSelect, driverTwoSelect, driverThreeSelect];

        allSelects.forEach(select => {
            select.addEventListener('change', updateOptions);
        });

        function updateOptions() {
            const selectedValues = new Set();
            
            allSelects.forEach(select => {
                if (select.value) {
                    selectedValues.add(select.value);
                }
            });

            allSelects.forEach(select => {
                Array.from(select.options).forEach(option => {
                    if (option.value && selectedValues.has(option.value) && option.value !== select.value) {
                        option.disabled = true;
                    } else {
                        option.disabled = false;
                    }
                });
            });
        }
    });
