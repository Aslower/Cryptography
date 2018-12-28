function sha3_with_check_out_size() {
						var chkObjs = document.getElementsByName("sha_3_out_size");
						var out_size = 512;
						for(var i=0;i<chkObjs.length;i++){
							if(chkObjs[i].checked){
								out_size = chkObjs[i].value;
								break;
							}
						}
						document.getElementById('sha_3_output').value = CryptoJS.SHA3(document.getElementById('sha_3_input').value, { outputLength:  out_size});
					}
				