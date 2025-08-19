# file: todo.py
import json, os, datetime

DATA_FILE = "todo_data.json"

def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(items):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

def show(items):
    if not items:
        print("\nNo tasks yet.\n"); return
    print("\nID | Done | Task                                   | Due")
    print("-"*70)
    for i, t in enumerate(items, 1):
        due = t.get("due", "")
        print(f"{i:>2} | {'✔' if t['done'] else ' '}    | {t['title'][:40]:40} | {due}")
    print()

def add(items):
    title = input("Task title: ").strip()
    if not title: return
    due = input("Due date (YYYY-MM-DD, optional): ").strip()
    if due:
        try: datetime.date.fromisoformat(due)
        except ValueError: print("Invalid date; leaving empty."); due = ""
    items.append({"title": title, "done": False, "due": due})

def complete(items):
    idx = int(input("Complete which ID? ") or 0)
    if 1 <= idx <= len(items): items[idx-1]["done"] = True

def edit(items):
    idx = int(input("Edit which ID? ") or 0)
    if 1 <= idx <= len(items):
        t = items[idx-1]
        new = input(f"New title [{t['title']}]: ").strip() or t["title"]
        due = input(f"New due [{t.get('due','')}]: ").strip() or t.get("due","")
        t.update({"title": new, "due": due})

def delete(items):
    idx = int(input("Delete which ID? ") or 0)
    if 1 <= idx <= len(items): items.pop(idx-1)

def clear_done(items):
    items[:] = [t for t in items if not t["done"]]

def main():
    items = load()
    actions = {
        "1": ("Show tasks", show),
        "2": ("Add task", add),
        "3": ("Mark complete", complete),
        "4": ("Edit task", edit),
        "5": ("Delete task", delete),
        "6": ("Clear completed", clear_done),
        "7": ("Save & Exit", None)
    }
    while True:
        print("\n=== TO-DO LIST ===")
        for k,(label,_) in actions.items(): print(f"{k}. {label}")
        choice = input("Choose: ").strip()
        if choice == "7":
            save(items); print("Saved. Bye!"); break
        action = actions.get(choice)
        if action:
            action[1](items)
        else:
            print("Invalid choice.")
        save(items)  # auto-save each step

if __name__ == "__main__":
    main()
