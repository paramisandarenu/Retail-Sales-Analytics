console.log("Retail Sales Dashboard JavaScript is connected.");

fetch("dashboard_data.json")
    .then(response => response.json())
    .then(data => {

        // ==============================
        // KPI VALUES
        // ==============================

        const totalRevenue = data.kpis.totalRevenue;
        const totalOrders = data.kpis.totalOrders;
        const averageOrderValue = data.kpis.averageOrderValue;
        const totalQuantity = data.kpis.totalQuantity;


        // ==============================
        // DISPLAY KPI VALUES
        // ==============================

        document.getElementById("totalRevenue").textContent =
            "LKR " + (totalRevenue / 1000000).toFixed(2) + "M";

        document.getElementById("totalOrders").textContent =
            totalOrders.toLocaleString();

        document.getElementById("averageOrder").textContent =
            "LKR " + averageOrderValue.toLocaleString(
                "en-US",
                {
                    maximumFractionDigits: 0
                }
            );

        document.getElementById("totalQuantity").textContent =
            totalQuantity.toLocaleString();


        // ==============================
        // 1. MONTHLY SALES TREND
        // ==============================

        const monthlyLabels = Object.keys(data.monthlySales);
        const monthlyValues = Object.values(data.monthlySales);

        new Chart(document.getElementById("monthlySalesChart"), {

            type: "line",

            data: {
                labels: monthlyLabels,

                datasets: [
                    {
                        label: "Monthly Sales (LKR)",
                        data: monthlyValues,

                        borderWidth: 3,

                        tension: 0.3,

                        fill: false,

                        pointRadius: 5,

                        pointHoverRadius: 8,

                        pointHitRadius: 15
                    }
                ]
            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                interaction: {
                    mode: "index",
                    intersect: false
                },

                plugins: {

                    legend: {
                        display: true
                    },

                    tooltip: {
                        enabled: true
                    }
                },

                scales: {

                    y: {
                        beginAtZero: true,

                        ticks: {
                            callback: function(value) {
                                return "LKR " +
                                    (value / 1000000).toFixed(1) +
                                    "M";
                            }
                        }
                    }
                }
            }
        });


        // ==============================
        // 2. SALES BY CATEGORY
        // ==============================

        const categoryLabels = Object.keys(data.categorySales);
        const categoryValues = Object.values(data.categorySales);

        new Chart(document.getElementById("categorySalesChart"), {

            type: "bar",

            data: {

                labels: categoryLabels,

                datasets: [
                    {
                        label: "Sales by Category (LKR)",
                        data: categoryValues,

                        borderWidth: 1
                    }
                ]
            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                interaction: {
                    mode: "index",
                    intersect: false
                },

                plugins: {

                    legend: {
                        display: true
                    },

                    tooltip: {
                        enabled: true,

                        callbacks: {

                            label: function(context) {

                                return "LKR " +
                                    context.raw.toLocaleString(
                                        "en-US",
                                        {
                                            maximumFractionDigits: 0
                                        }
                                    );
                            }
                        }
                    }
                },

                scales: {

                    y: {

                        beginAtZero: true,

                        ticks: {

                            callback: function(value) {

                                return "LKR " +
                                    (value / 1000000).toFixed(1) +
                                    "M";
                            }
                        }
                    }
                }
            }
        });


        // ==============================
        // 3. SALES BY CITY
        // ==============================

        const cityLabels = Object.keys(data.citySales);
        const cityValues = Object.values(data.citySales);

        new Chart(document.getElementById("citySalesChart"), {

            type: "bar",

            data: {

                labels: cityLabels,

                datasets: [
                    {
                        label: "Sales by City (LKR)",
                        data: cityValues,

                        borderWidth: 1
                    }
                ]
            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                interaction: {
                    mode: "index",
                    intersect: false
                },

                plugins: {

                    legend: {
                        display: true
                    },

                    tooltip: {
                        enabled: true,

                        callbacks: {

                            label: function(context) {

                                return "LKR " +
                                    context.raw.toLocaleString(
                                        "en-US",
                                        {
                                            maximumFractionDigits: 0
                                        }
                                    );
                            }
                        }
                    }
                },

                scales: {

                    y: {

                        beginAtZero: true,

                        ticks: {

                            callback: function(value) {

                                return "LKR " +
                                    (value / 1000000).toFixed(1) +
                                    "M";
                            }
                        }
                    }
                }
            }
        });


        // ==============================
        // 4. TOP 10 PRODUCTS
        // ==============================

        const productLabels = Object.keys(data.topProducts);
        const productValues = Object.values(data.topProducts);

        new Chart(document.getElementById("topProductsChart"), {

            type: "bar",

            data: {

                labels: productLabels,

                datasets: [
                    {
                        label: "Quantity Sold",
                        data: productValues,

                        borderWidth: 1
                    }
                ]
            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                interaction: {
                    mode: "index",
                    intersect: false
                },

                plugins: {

                    legend: {
                        display: true
                    },

                    tooltip: {
                        enabled: true,

                        callbacks: {

                            label: function(context) {

                                return "Quantity: " +
                                    context.raw.toLocaleString();
                            }
                        }
                    }
                },

                scales: {

                    y: {

                        beginAtZero: true,

                        ticks: {
                            stepSize: 50
                        }
                    }
                }
            }
        });


        console.log("All dashboard charts loaded successfully.");

    })

    .catch(error => {

        console.error(
            "Error loading dashboard data:",
            error
        );

    });