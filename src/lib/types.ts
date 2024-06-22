// src/lib/types.ts

export interface User {
    id: number;
    name: string;
    email: string;
    student_id: string;
    created_at: string;
    updated_at: string;
}

export interface Group {
    id: number;
    name: string;
    description?: string;
}

export interface Role {
    role_id: number;
    role_name: string;
}

export interface Event {
    id: number;
    name: string;
    description?: string;
    datetime: string;
    location?: string;
    group_id: number;
    duration?: string;
}

export interface UserGroup {
    user_id: number;
    group_id: number;
    role_id: number;
}

export interface Attendance {
    user_id: number;
    group_id: number;
    event_id: number;
    attendance_date: string;
    attendance_time: string;
}

export interface EventsData {
    events: Event[];
}
