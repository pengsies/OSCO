<!-- src/lib/EventCard.svelte -->
<script lang="ts">
    import type { Event } from '$lib/types';
    export let event: Event;

    // Function to format date and time
    function formatDateTime(dateTime: string): string {
        const date = new Date(dateTime);
        return date.toLocaleString();
    }
</script>

<div class="col mb-4">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{event.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{formatDateTime(event.starttime)}</h6>
            {#if event.endtime}
                <h6 class="card-subtitle mb-2 text-muted">{formatDateTime(event.endtime)}</h6>
            {/if}
            <p class="card-text">{event.description}</p>
            <p class="card-text"><small class="text-muted">{event.location}</small></p>
            <p class="card-text"><small class="text-muted">{event.GROUP.name}</small></p>
        </div>
    </div>
</div>
