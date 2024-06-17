// src/routes/events/+page.server.js
import { supabase } from '$lib/supabaseClient';

export async function load() {
    try {
        const { data: events, error } = await supabase
            .from('EVENT')
            .select(`
                id,
                name,
                description,
                starttime,
                location,
                group_id,
                endtime,
                GROUP (
                    name
                )
            `);

        if (error) {
            console.error('Error fetching events:', error);
            return {
                status: 500,
                error: new Error('Failed to fetch events'),
            };
        }

        console.log('Fetched events:', events);

        return {
            events: events ?? [],
        };
    } catch (err) {
        console.error('Unexpected error:', err);
        return {
            status: 500,
            error: new Error('Unexpected error occurred'),
        };
    }
}
