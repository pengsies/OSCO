<!-- src/routes/events/+page.svelte -->
<script lang="ts">
    import EventCard from '$lib/EventCard.svelte';
    import type { EventsData } from '$lib/types';

    export let data: EventsData;
</script>

<section class="py-5">
    <div class="container py-5">
        <div class="row mb-5">
            <div class="col-md-8 col-xl-6 col-xxl-5 text-center mx-auto">
                <h2 class="fw-bold">Upcoming Events</h2>
                <p class="text-muted" style="margin-left: 0px; padding-left: 0px; padding-right: 0px;">
                    Find out about the latest events from the Interest Groups and join them to learn and have fun
                </p>
            </div>
        </div>
        <div class="row row-cols-1 row-cols-md-2 mx-auto" style="max-width: 900px;">
            {#if data && data.events}
                {#each data.events as event}
                    <EventCard {event} />
                {/each}
            {:else}
                <p>No events available.</p>
            {/if}
        </div>
    </div>
</section>
