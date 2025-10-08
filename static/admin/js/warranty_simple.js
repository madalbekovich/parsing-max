document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.button');

    buttons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmAction = confirm('Вы уверены, что хотите использовать гарантию для этого устройства?');
            if (!confirmAction) {
                event.preventDefault();
            }
        });
    });
});
