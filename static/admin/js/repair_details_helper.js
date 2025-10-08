// Скрипт форматирования деталей ремонта для Jazzmin
(function() {
    'use strict';
    
    function initRepairDetailsLayout() {
        console.log('🔍 Поиск деталей ремонта в Jazzmin Admin...');
        
        // Ищем строки с полями деталей ремонта
        const repairFields = [
            'display',
            'case', 
            'cover',
            'general_360',
            'side',
            'lens'
        ];
        
        const repairRows = [];
        
        // Находим каждую строку по основному чекбоксу
        repairFields.forEach(fieldName => {
            const checkbox = document.querySelector(`input[name="${fieldName}"][type="checkbox"]`);
            if (checkbox) {
                // Ищем родительский .row контейнер
                const row = checkbox.closest('.row');
                if (row && !repairRows.includes(row)) {
                    repairRows.push(row);
                    row.setAttribute('data-repair-field', fieldName);
                    console.log(`✅ Найдена строка для: ${fieldName}`);
                }
            }
        });
        
        if (repairRows.length === 0) {
            console.error('❌ Не найдено строк с деталями ремонта');
            return;
        }
        
        console.log(`🎯 Найдено ${repairRows.length} строк для форматирования`);
        
        // Находим родительский контейнер (карточку) для всех строк
        const parentCard = repairRows[0].closest('.card, .card-body, [class*="card"]');
        if (parentCard) {
            parentCard.classList.add('repair-details-container');
            console.log('✅ Добавлен класс к родительскому контейнеру');
        }
        
        // Обрабатываем каждую строку
        repairRows.forEach((row, index) => {
            processRepairRow(row, index);
        });
        
        // Добавляем разделители
        setTimeout(() => addSeparators(repairRows), 100);
        
        console.log('🎉 Форматирование завершено!');
    }
    
    function processRepairRow(row, index) {
        console.log(`🔧 Обработка строки ${index}: ${row.getAttribute('data-repair-field')}`);
        
        // Добавляем класс
        row.classList.add('repair-detail-row');
        row.setAttribute('data-repair-index', index);
        
        // Находим все поля внутри строки
        const fields = row.querySelectorAll('.fieldBox, .col-auto, [class*="field-"]');
        console.log(`   📦 Найдено полей: ${fields.length}`);
        
        // Применяем Grid Layout к строке
        row.style.cssText = `
            display: grid !important;
            grid-template-columns: 180px repeat(${fields.length - 1}, 1fr) !important;
            gap: 15px !important;
            padding: 20px 15px !important;
            background-color: #f8f9fa !important;
            border-radius: 8px !important;
            margin-bottom: 50px !important;
            margin-top: 0 !important;
            border-left: 4px solid #007bff !important;
            align-items: start !important;
            transition: all 0.2s ease !important;
        `;
        
        // Hover эффекты
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#e9ecef';
            this.style.boxShadow = '0 4px 12px rgba(0, 123, 255, 0.15)';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#f8f9fa';
            this.style.boxShadow = 'none';
        });
        
        // Focus эффект
        row.addEventListener('focusin', function() {
            this.style.borderLeftColor = '#0056b3';
            this.style.boxShadow = '0 4px 12px rgba(0, 123, 255, 0.25)';
        });
        
        row.addEventListener('focusout', function() {
            this.style.borderLeftColor = '#007bff';
            this.style.boxShadow = 'none';
        });
        
        // Обрабатываем каждое поле
        fields.forEach((field, fieldIndex) => {
            processField(field, fieldIndex);
        });
        
        console.log(`   ✅ Строка ${index} отформатирована`);
    }
    
    function processField(field, fieldIndex) {
        // Убираем Bootstrap классы, которые мешают
        field.classList.remove('col-auto', 'col', 'col-md-auto');
        
        // Применяем flex layout к полю
        field.style.cssText = `
            display: flex !important;
            flex-direction: column !important;
            gap: 8px !important;
            margin: 0 !important;
            padding: 0 !important;
        `;
        
        // Обработка label
        const label = field.querySelector('label');
        if (label) {
            // Убираем двоеточие
            const text = label.textContent.trim();
            if (text.endsWith(':')) {
                label.textContent = text.slice(0, -1);
            }
            
            label.style.cssText = `
                font-weight: 600 !important;
                color: #495057 !important;
                font-size: 13px !important;
                margin: 0 0 5px 0 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.5px !important;
                white-space: nowrap !important;
                display: block !important;
            `;
            
            // Первое поле (название запчасти) - особое форматирование
            if (fieldIndex === 0) {
                label.style.color = '#007bff';
                label.style.fontSize = '15px';
                label.style.fontWeight = '700';
            }
        }
        
        // Обработка checkbox
        const checkbox = field.querySelector('input[type="checkbox"]');
        if (checkbox) {
            checkbox.style.cssText = `
                width: 24px !important;
                height: 24px !important;
                cursor: pointer !important;
                margin: 5px 0 !important;
            `;
            
            // Цвет в зависимости от состояния
            const updateColor = () => {
                checkbox.style.accentColor = checkbox.checked ? '#28a745' : '#007bff';
            };
            updateColor();
            checkbox.addEventListener('change', updateColor);
            
            // Анимация при наведении
            checkbox.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.1)';
                this.style.transition = 'transform 0.15s ease';
            });
            
            checkbox.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
        }
        
        // Обработка date input
        const dateInput = field.querySelector('input[type="date"]');
        if (dateInput) {
            dateInput.style.cssText = `
                padding: 8px 12px !important;
                border: 2px solid #ced4da !important;
                border-radius: 6px !important;
                font-size: 14px !important;
                width: 100% !important;
                max-width: 200px !important;
                background-color: #ffffff !important;
                transition: all 0.2s ease !important;
            `;
            
            dateInput.addEventListener('focus', function() {
                this.style.borderColor = '#007bff';
                this.style.boxShadow = '0 0 0 0.2rem rgba(0, 123, 255, 0.15)';
            });
            
            dateInput.addEventListener('blur', function() {
                this.style.borderColor = '#ced4da';
                this.style.boxShadow = 'none';
            });
        }
        
        // Обработка readonly input
        const readonlyInput = field.querySelector('input[readonly], input[disabled]');
        if (readonlyInput) {
            readonlyInput.style.cssText = `
                background-color: #e9ecef !important;
                color: #6c757d !important;
                padding: 8px 12px !important;
                border-radius: 6px !important;
                font-size: 14px !important;
                width: 100% !important;
                max-width: 200px !important;
                border: 2px solid #dee2e6 !important;
                text-align: center !important;
                cursor: not-allowed !important;
                font-weight: 500 !important;
            `;
            
            // Плейсхолдер для пустых полей
            if (!readonlyInput.value || readonlyInput.value.trim() === '') {
                readonlyInput.value = '—';
                readonlyInput.style.color = '#adb5bd';
            }
        }
        
        // Обработка обычных text input (если есть)
        const textInput = field.querySelector('input[type="text"]:not([readonly])');
        if (textInput) {
            textInput.style.cssText = `
                padding: 8px 12px !important;
                border: 2px solid #ced4da !important;
                border-radius: 6px !important;
                font-size: 14px !important;
                width: 100% !important;
                transition: all 0.2s ease !important;
            `;
        }
    }
    
    function addSeparators(rows) {
        rows.forEach((row, index) => {
            if (index < rows.length - 1 && !row.dataset.separatorAdded) {
                const separator = document.createElement('div');
                separator.className = 'repair-separator';
                separator.style.cssText = `
                    grid-column: 1 / -1 !important;
                    width: 100% !important;
                    height: 1px !important;
                    background: linear-gradient(to right, transparent, #dee2e6 50%, transparent) !important;
                    margin: -30px 0 5px 0 !important;
                `;
                
                // Вставляем после текущей строки
                if (row.nextElementSibling) {
                    row.parentNode.insertBefore(separator, row.nextElementSibling);
                } else {
                    row.parentNode.appendChild(separator);
                }
                
                row.dataset.separatorAdded = 'true';
            }
        });
    }
    
    // Поддержка темной темы
    function applyDarkTheme() {
        const isDark = document.body.classList.contains('dark-mode') || 
                       document.body.getAttribute('data-bs-theme') === 'dark';
        
        if (isDark) {
            const rows = document.querySelectorAll('.repair-detail-row');
            rows.forEach(row => {
                row.style.backgroundColor = '#2d3748';
                row.style.borderLeftColor = '#4299e1';
                
                row.addEventListener('mouseenter', function() {
                    this.style.backgroundColor = '#374151';
                });
                
                row.addEventListener('mouseleave', function() {
                    this.style.backgroundColor = '#2d3748';
                });
            });
        }
    }
    
    // Адаптивность
    function applyResponsiveLayout() {
        const width = window.innerWidth;
        const rows = document.querySelectorAll('.repair-detail-row');
        
        rows.forEach(row => {
            const fields = row.querySelectorAll('[class*="field"]').length;
            
            if (width < 768) {
                // Мобильные: одна колонка
                row.style.gridTemplateColumns = '1fr';
            } else if (width < 1200) {
                // Планшеты: 2 колонки
                row.style.gridTemplateColumns = '150px 1fr';
            } else {
                // Десктоп: полная сетка
                row.style.gridTemplateColumns = `180px repeat(${fields - 1}, 1fr)`;
            }
        });
    }
    
    // Основная инициализация
    function init() {
        console.log('📝 Скрипт форматирования деталей ремонта запущен');
        initRepairDetailsLayout();
        applyDarkTheme();
        applyResponsiveLayout();
    }
    
    // Запуск при загрузке
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        setTimeout(init, 100);
    }
    
    // Адаптивность при изменении размера окна
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(applyResponsiveLayout, 150);
    });
    
    // Наблюдатель за динамическими изменениями
    const observer = new MutationObserver(function(mutations) {
        let shouldReinit = false;
        
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1 && (
                    node.classList?.contains('row') ||
                    node.querySelector?.('.row') ||
                    node.querySelector?.('input[type="checkbox"]')
                )) {
                    shouldReinit = true;
                }
            });
        });
        
        if (shouldReinit) {
            console.log('🔄 Обнаружены изменения, переинициализация...');
            setTimeout(init, 100);
        }
    });
    
    if (document.body) {
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }
    
})();