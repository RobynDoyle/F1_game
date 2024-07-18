document.addEventListener('DOMContentLoaded', function () {
    const colors = [
        '#FFFFFF', '#FFFEFE', '#FFFDFD', '#FFFCFC', '#FFFBFB', '#FFFAFA', '#FFF9F9', '#FFF8F8', '#FFF7F7', '#FFF6F6',
        '#FFF5F5', '#FFF4F4', '#FFF3F3', '#FFF2F2', '#FFF1F1', '#FFF0F0', '#FFEFEF', '#FFEDED', '#FFECEC', '#FFEAEA',
        '#FFE9E9', '#FFE8E8', '#FFE6E6', '#FFE5E5', '#FFE3E3', '#FFE2E2', '#FFE0E0', '#FFDFDF', '#FFDCDC', '#FFDADA',
        '#FFD8D8', '#FFD5D5', '#FFD3D3', '#FFD1D1', '#FFCECE', '#FFCCCC', '#FFC9C9', '#FFC7C7', '#FFC4C4', '#FFC2C2',
        '#FFBFBF', '#FFBDBD', '#FFB8B8', '#FFB6B6', '#FFB3B3', '#FFB1B1', '#FFADAD', '#FFAAAA', '#FFA7A7', '#FFA3A3',
        '#FFA0A0', '#FF9D9D', '#FF9999', '#FF9696', '#FF9292', '#FF8F8F', '#FF8B8B', '#FF8787', '#FF8383', '#FF8080',
        '#FF7C7C', '#FF7878', '#FF7474', '#FF7070', '#FF6B6B', '#FF6767', '#FF6363', '#FF5E5E', '#FF5A5A', '#FF5555',
        '#FF5151', '#FF4C4C', '#FF4747', '#FF4343', '#FF3E3E', '#FF3939', '#FF3434', '#FF2E2E', '#FF2929', '#FF2424',
        '#FF1F1F', '#FF1919', '#FF1414', '#FF0E0E', '#FF0909', '#FF0404', '#FF0000', '#F70000', '#EF0000', '#E70000',
        '#DF0000', '#D70000', '#CF0000', '#C70000', '#BF0000', '#B70000', '#AF0000', '#A70000', '#9F0000', '#970000',
        '#8F0000', '#870000', '#7F0000', '#770000', '#6F0000', '#670000', '#5F0000', '#570000', '#4F0000', '#470000',
        '#3F0000', '#370000', '#2F0000', '#270000', '#1F0000', '#170000', '#0F0000', '#070000', '#000000'
    ];

    const heading = document.getElementById('colorful-heading');
    let currentIndex = 0;

    function changeColor() {
        heading.style.color = colors[currentIndex];
        currentIndex = (currentIndex + 1) % colors.length; // Move to the next color, looping back to the start if necessary
    }

    changeColor();
    setInterval(changeColor, 50); // Repeat color change every .5 seconds
});
