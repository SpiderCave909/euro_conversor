import tkinter as tk;

def main():
    background = "#f1f5f2";
    app = tk.Tk();
    app.title("Euro Converter");
    app.geometry("480x420");
    app.configure(bg=background);

    currencies = ("EUR", "USD", "GBP", "JPY", "CHF");
    from_currency = tk.StringVar(value="EUR");
    to_currency = tk.StringVar(value="USD");

    page = tk.Frame(app, bg=background, padx=28, pady=24);
    page.pack(fill="both", expand=True);

    tk.Label(page, text="Euro Converter", bg=background, fg="#203c35", font=("Segoe UI", 22, "bold")).pack(anchor="w");

    tk.Label(page, text="Select the currencies you want to convert between.", bg=background, fg="#687a73", font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 18));

    card = tk.Frame(page, bg="white", padx=20, pady=20);
    card.pack(fill="x");

    choices = tk.Frame(card, bg="white");
    choices.pack(fill="x");
    choices.columnconfigure(0, weight=1);
    choices.columnconfigure(1, weight=1);

    for column, label, currency in ((0, "FROM", from_currency), (1, "TO", to_currency)):
        selector = tk.Frame(choices, bg="white");
        selector.grid(row=0, column=column, sticky="ew", padx=(0, 8) if column == 0 else (8, 0));

        tk.Label(selector, text=label, bg="white", fg="#52665e", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 6));

        menu_button = tk.OptionMenu(selector, currency, *currencies);
        menu_button.configure(
            bg="#f7faf8",
            fg="#203c35",
            activebackground="#e5eee8",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#dce5df",
            font=("Segoe UI", 10),
            padx=8,
            pady=6
        );
        menu_button["menu"].configure(font=("Segoe UI", 10));
        menu_button.pack(fill="x");

    result_box = tk.Frame(card, bg="#edf5f0", padx=14, pady=12);
    result_box.pack(fill="x", pady=(20, 14));

    tk.Label(result_box, text="RESULT", bg="#edf5f0", fg="#687a73", font=("Segoe UI", 9, "bold")).pack(anchor="w");

    tk.Label(result_box, text="Your result will appear here", bg="#edf5f0", fg="#176b55", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(5, 0));

    tk.Button(
        card,
        text="Convert",
        bg="#176b55",
        fg="white",
        activebackground="#125541",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2",
        pady=9
    ).pack(fill="x");

    app.mainloop();


if __name__ == "__main__":
    main();