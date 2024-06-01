const {createApp, ref}= Vue;

      const app = createApp({
            setup(){



                const espStatus = ref("");
                const updateESPstatus = async () =>{
                    try{
                        const response = await fetch('/update_esp', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            }
                            
                        }); 
                        const data = await response.json();
                        console.log(data);
                         espStatus.value = data.response;
                         console.log(espStatus.value);
                    } catch(error){
                        console.error('Error:', error);
                    };

                };

                return {updateESPstatus, espStatus};

            },
            watch: {
                
                
            }
        });

        app.mount('#app');
    

