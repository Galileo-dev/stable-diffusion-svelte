<script>
</script>

<div class="hist">
  <div class="collection-panel">
    {#each Array(20) as _, i}
      <div class="list-row">
        {#each Array(4) as _, i}
          <div class="hist-gen-img">
            <div class="archive-img">
              <img src="" />
            </div>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  .hist {
    height: 100%;
    overflow-y: auto;

    padding: 20px;
  }

  .archive-img {
    background: var(--b20);
    background-clip: padding-box;
    overflow: hidden;
    padding-top: 100%;
    position: relative;
  }

  .hist-gen-img {
    background: var(--b20);

    overflow: hidden;
    position: relative;
  }

  img {
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
  }

  .list-row {
    grid-gap: 4px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    width: auto;
    opacity: 1;
    transition: opacity 0.4s;
    list-style: none;
    margin-top: 24px;
  }

  .hist-gen-img {
    width: 37px;
    height: 37px;
  }

  @media only screen and (max-width: 600px) {
    .collection-panel {
      display: flex;
      flex-direction: row;
    }

    .hist {
      overflow-x: auto;
      padding: 5px;
    }

    .hist-gen-img {
      width: 37px;
      height: 37px;
    }

    .list-row {
      grid-gap: 4px;
      display: grid;
      grid-template-columns: none;
      grid-template-rows: repeat(4, 1fr);
      width: 100%;
      margin-right: 25px;
      margin-top: 0;
    }
  }
</style>
