build: 
	java -jar apktool_2.7.0.jar b ${dir} -out tampered.apk

align: build
	zipalign -p 4 tampered.apk unsigned.apk

createkey: align

	@if test -f myks.jks; then \
        echo "Keystore already exists"; \
    else \
        echo "Creating keystore..."; \
	 	keytool -genkey -v -noprompt \
  		-alias myalias \
  		-dname "CN=mydomain.com, OU=MyOrgUnit, O=MyOrg, L=MyCity, S=MyState, C=MyCountry" \
  		-keystore myks.jks \
  		-storepass ${pass} \
  		-keypass ${pass} \
  		-keyalg RSA \
  		-keysize 2048 \
  		-validity 3650; \
    fi
        
sign: createkey
	apksigner sign --ks myks.jks \
  	--ks-key-alias myalias \
  	--ks-pass pass:${pass} \
  	--key-pass pass:${pass} \
  	--out signed.apk \
  	--v1-signing-enabled false \
  	unsigned.apk

recompile: sign
