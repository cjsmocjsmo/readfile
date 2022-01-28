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
        python3-openpyxl \
		nano

COPY kitsap.sh /home/
COPY mason.sh /home/
COPY pierce.sh /home/
COPY AllMailLists.py /home/
COPY kitsapmaillists.py /home/
COPY masonmaillists.py /home/
COPY piercemaillists.py /home/


RUN chmod 0655 "/home/AllMailLists.py" && \
	chmod 0655 "/home/kitsapmaillists.py" && \
	chmod 0655 "/home/masonmaillists.py" && \
	chmod 0655 "/home/piercemaillists.py" && \
    chmod 0655 "/home/kitsap.sh" && \
	chmod 0655 "/home/mason.sh" && \
	chmod 0655 "/home/pierce.sh"

CMD sh -c 'trap "exit" TERM; while true; do sleep 1; done'