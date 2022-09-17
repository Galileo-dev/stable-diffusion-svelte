<script>
  import { onMount } from "svelte";
  import ImagePrompt from "./components/ImagePrompt.svelte";
  import ImageUpload from "./components/ImageUpload.svelte";
  import ImageView from "./components/ImageView.svelte";
  import Nav from "./components/Nav.svelte";
  import ServerURl from "./components/ServerURl.svelte";
  import { auth } from "./api";
  import { IP, Session } from "./store.js";
  import ImageCollection from "./components/ImageCollection.svelte";
  import Fa from "svelte-fa";
  import { faArrowCircleRight } from "@fortawesome/free-solid-svg-icons";
  onMount(async () => {
    await auth();
    fetch($IP + "/whoami", {
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });

  function togglePanel() {
    isDrawerOpen = !isDrawerOpen;
    console.log(isDrawerOpen);
  }

  let isDrawerOpen = false;
</script>

<main>
  <div class="main-interface">
    <div class="page-wrapper">
      <Nav />
      <div class="page-main">
        <div class="container page scroll-able">
          <div class="create-page">
            <!-- <ServerURl /> -->
            <div
              class="drawer-icon {isDrawerOpen ? 'drawer-icon-open' : ''}"
              on:click={() => togglePanel()}
            >
              <Fa icon={faArrowCircleRight} size="2rem" />
            </div>

            <ImagePrompt />
            <ImageUpload />
            <ImageView />
          </div>
        </div>
        <div class="side-panel {isDrawerOpen ? '' : 'side-panel-close'} ">
          <ImageCollection isOpen={isDrawerOpen} />
        </div>
      </div>
    </div>
  </div>
</main>

<style>
  .drawer-icon {
    position: absolute;
    top: 0;
    right: 0;
    margin: 20px;
    transition: ease 0.5s;
  }

  .drawer-icon:hover {
    transform: scale(1.25);
  }

  .drawer-icon.drawer-icon-open {
  }

  .page-main {
    display: flex;
    flex: 1 1 auto;
    overflow-x: hidden;
    overflow-y: auto;
    position: relative;
  }

  .page-wrapper {
    align-items: stretch;
    background-color: var(--page-background-color);
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow-x: hidden;
  }

  .create-page {
    padding-top: 180px;
    padding-bottom: 50px;
  }

  .side-panel {
    background-color: var(--b15);
    border-left: 1px solid rgba(34, 34, 34, 0.05);
    /* transition: 200ms ease; */
    z-index: 1;
  }

  @media only screen and (min-width: 600px) {
    .side-panel {
      width: 200px;
      transition: width 200ms ease-in-out;
    }

    .side-panel-close {
      width: 0px;
      overflow: hidden;
      /* display: none; */
    }
  }

  @media only screen and (max-width: 600px) {
    .page-main {
      flex-direction: column;
    }

    .side-panel {
      bottom: 0;
      width: 100vw;
      height: 200px;
      transition: height 200ms ease-in-out;

      /* height: 10px; */
    }

    .side-panel-close {
      /* display: none; */
      height: 0px;
      overflow: hidden;
    }
  }

  .side-panel-close {
    /* display: none; */
    height: 0px;
    overflow: hidden;
  }

  .scroll-able {
    margin: 0 auto;
  }
  .main-interface {
    /* display: flex;
    flex: 1 1 auto;
    overflow-x: hidden;
    overflow-y: hidden;
    position: relative; */
    height: 100%;
    position: relative;
    z-index: 1;
  }

  .container {
    text-align: center;
    overflow-y: auto;
    padding: 20px;
    margin: 0 auto;
    flex-direction: column;
    height: 100%;
  }

  .page {
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    position: relative;
    width: 100%;
  }

  h1 {
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
  main {
    /* max-width: none;
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;

    align-items: stretch;
    background-color: var(--page-background-color);
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow-x: hidden; */
    height: 100%;

    overflow: auto;
  }
</style>
