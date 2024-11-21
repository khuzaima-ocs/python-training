export type TodoStatus = "pending" | "in-progress" | "completed" | "removed" 

export type Todo = {
    id: number;
    title: string;
    description: string;
    status: TodoStatus
}