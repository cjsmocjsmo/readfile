FROM debian:bullseye

RUN \
	apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get autoclean -y && \
	apt-get autoremove -y && \
	apt-get install --no-install-recommends -y \
        ca-certificates \
		wget \
		unzip \
        python3-pandas \
        python3-openpyxl 

COPY kitsap.sh /home/
COPY mason.sh /home/
COPY pierce.sh /home/
COPY readlines.py /home/


RUN chmod 0655 "/home/readlines.py" && \
    chmod 0655 "/home/kitsap.sh" && \
	chmod 0655 "/home/mason.sh" && \
	chmod 0655 "/home/pierce.sh"

# RUN /home/kitsap.sh
# RUN /home/mason.sh
# RUN /home/pierce.sh
# RUN python3 /home/readlines.py

CMD sh -c 'trap "exit" TERM; while true; do sleep 1; done'